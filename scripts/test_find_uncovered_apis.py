import unittest

from scripts.find_uncovered_apis import parse_signature


class ParseSignatureTests(unittest.TestCase):
    def test_member_with_initializer_method_call_is_member(self) -> None:
        sig = (
            "public static readonly DirectProperty<TopLevel, Size> ClientSizeProperty "
            "= AvaloniaProperty.RegisterDirect<TopLevel, Size>(nameof(ClientSize), o => o.ClientSize);"
        )
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "member")
        self.assertEqual(symbol, "ClientSizeProperty")

    def test_record_struct_parses_real_type_name(self) -> None:
        sig = "public record struct DispatcherProcessingDisabled : IDisposable"
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "type")
        self.assertEqual(symbol, "DispatcherProcessingDisabled")

    def test_record_parses_real_type_name(self) -> None:
        sig = "public sealed record ThemeVariant"
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "type")
        self.assertEqual(symbol, "ThemeVariant")

    def test_operator_signature_is_operator(self) -> None:
        sig = "public static explicit operator ThemeVariant(PlatformThemeVariant themeVariant) {"
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "operator")
        self.assertEqual(symbol, "ThemeVariant")

    def test_tuple_generic_property_is_member_not_method(self) -> None:
        sig = "public IObservable<(object, RoutedEventArgs)> Raised => _raised;"
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "member")
        self.assertEqual(symbol, "Raised")

    def test_constructor_with_base_initializer_is_method(self) -> None:
        sig = (
            "public CancelRoutedEventArgs(RoutedEvent? routedEvent, object? source) "
            ": base(routedEvent, source) {"
        )
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "method")
        self.assertEqual(symbol, "CancelRoutedEventArgs")

    def test_generic_method_with_where_constraint_is_method(self) -> None:
        sig = (
            "public static RoutedEvent<TEventArgs> Register<TOwner, TEventArgs>( "
            "string name, RoutingStrategies routingStrategy) where TEventArgs : RoutedEventArgs {"
        )
        kind, symbol = parse_signature(sig)
        self.assertEqual(kind, "method")
        self.assertEqual(symbol, "Register")


if __name__ == "__main__":
    unittest.main()
